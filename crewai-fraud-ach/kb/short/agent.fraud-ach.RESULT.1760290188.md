```json
{
  "id": "2b0d3ae1c4f31e09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290188,
  "host_pid": "9e6742732c60:1",
  "hash": "13fb7e8029d2602758042f026ad2a0eb9ba50cee7ee83bfaa65f60c8aa44cb9b",
  "cid": "QmV113fb7e8029d2602758042f026ad2a0eb9ba50cee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290188,
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
      "evaluated_at": 1760290188
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
  "sig": "398221e1583e2f92dc197eb1e42e8bcb9f2f8ec49dd1785bce5748b45803cdea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596228343
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 14400000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '964edcfaddb10414'}}}