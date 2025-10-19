```json
{
  "id": "b850bb00f11ec53c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287544,
  "host_pid": "9e6742732c60:1",
  "hash": "4c196c99df8918048886982ab1c3120c36e24b613092fcdb54a5b45fc3b8b256",
  "cid": "QmV14c196c99df8918048886982ab1c3120c36e24b61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287544,
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
      "evaluated_at": 1760287544
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
  "sig": "3afb9bc32ea98e919564a0c0ab660980a200f81e000c829ada3b44b6b16f0ae4"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 063100277559927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285763, 'matching_hash': '07b51054ae5371fb'}}}een': 1760285763, 'matching_hash': 'bfc9cdfd9eceb164'}}}