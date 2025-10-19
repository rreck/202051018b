```json
{
  "id": "66ee3760a38c0fce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288298,
  "host_pid": "9e6742732c60:1",
  "hash": "77951f807872a1cbb18dfaae5081299f1083179f609879c9ada1a21670495652",
  "cid": "QmV177951f807872a1cbb18dfaae5081299f1083179f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288298,
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
      "evaluated_at": 1760288298
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
  "sig": "b1ed5274f8122c3489f74c58cc7c504bcde7f90f6fcafd33bdb596ff2f4eb7cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278849424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 25496631, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': '586e1ac2088494e1'}}}