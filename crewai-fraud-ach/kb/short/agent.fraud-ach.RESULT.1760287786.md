```json
{
  "id": "dc37cfa9200b6b3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287786,
  "host_pid": "9e6742732c60:1",
  "hash": "35cd8deee7d45a69839303ff59d30a1f79895fa9c24e306f17fa1e75acdcae12",
  "cid": "QmV135cd8deee7d45a69839303ff59d30a1f79895fa9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287786,
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
      "evaluated_at": 1760287786
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
  "sig": "e32f6b6bf3c43dc489de6caee08c6514b87f42e55780cb3dec630630bfc8c31b"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 31026744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}