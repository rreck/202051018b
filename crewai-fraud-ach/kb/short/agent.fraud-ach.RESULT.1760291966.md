```json
{
  "id": "cf7cccb12cba7047",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291966,
  "host_pid": "9e6742732c60:1",
  "hash": "8a69e841d45428d1ef89bd64ba0fcfb91dade748a8dceacf024a7ba747875cba",
  "cid": "QmV18a69e841d45428d1ef89bd64ba0fcfb91dade748",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291966,
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
      "evaluated_at": 1760291966
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
  "sig": "4b035fe740136be5659a0647686095267a0ba46aadff0536982d9a277625efc5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274268796
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 48460489, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': 'ac75b07ed83ae58c'}}}