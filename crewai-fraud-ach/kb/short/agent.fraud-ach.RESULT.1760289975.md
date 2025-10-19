```json
{
  "id": "ea3d2df997578761",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289975,
  "host_pid": "9e6742732c60:1",
  "hash": "b54653e7eac4cb55a54073da2483e13e277319f8be588bda290f3d0e426780f4",
  "cid": "QmV1b54653e7eac4cb55a54073da2483e13e277319f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289975,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760289975
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "b5568f567c4e12cebb2f00d085fb74159d1b733e52f03c74b82624e9e6c4feac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153734827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 68095410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285764, 'matching_hash': 'f575a9f929aab221'}}}