```json
{
  "id": "8cf360c875a71169",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291317,
  "host_pid": "9e6742732c60:1",
  "hash": "150295eb8f33aae610f162b91fd74798ae8f2fd387585ab44309ece1b9f7e89a",
  "cid": "QmV1150295eb8f33aae610f162b91fd74798ae8f2fd3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291317,
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
      "evaluated_at": 1760291317
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
  "sig": "72e7ddf195d2514ced7ed60f53cf0e3a0f5bc4e56bf853195d4df859f4607b66"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029354583
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 13646136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': 'dbced9ae96be05e0'}}}