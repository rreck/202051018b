```json
{
  "id": "67b89c90a6b2927f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287691,
  "host_pid": "9e6742732c60:1",
  "hash": "6a1a675ee1f3254a7e2de29d0e3ca50cc30284cd2dd8cc1ede2b91dea79892a9",
  "cid": "QmV16a1a675ee1f3254a7e2de29d0e3ca50cc30284cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287691,
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
      "evaluated_at": 1760287691
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
  "sig": "aa268fe377eccaeda3ff76d58a8d2bf49bca277b86851d9b2188ea99975350ea"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 063100273021249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 33274905, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285764, 'matching_hash': '8f9c0aaacb6951b9'}}}