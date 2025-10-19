```json
{
  "id": "445c9de0bd9cd41b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288253,
  "host_pid": "9e6742732c60:1",
  "hash": "c55e36fdc71d7d438d5120e3b63787f2d8b542c79bc300dcd5523fd1f6159441",
  "cid": "QmV1c55e36fdc71d7d438d5120e3b63787f2d8b542c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288253,
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
      "evaluated_at": 1760288253
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
  "sig": "de54b7f40ccb0342b2236fd11c3a9ca96cfe2414711778bb10a66bfdb7e852ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 27687576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}