```json
{
  "id": "4ace7d9c17a7a05b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288330,
  "host_pid": "9e6742732c60:1",
  "hash": "898020bdc4e910dddb6cd90df57fa9edd216fd69ab8b4b3375a2824cd2e6b69d",
  "cid": "QmV1898020bdc4e910dddb6cd90df57fa9edd216fd69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288330,
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
      "evaluated_at": 1760288330
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
  "sig": "32238ba23a36efab05d793d8ef9e941c35bf2b9d850b825a062b265d0644a5b7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026087105
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 26392590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': '109bc77652f62494'}}}