```json
{
  "id": "c76c171d35304823",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289659,
  "host_pid": "9e6742732c60:1",
  "hash": "91ca88761bbf3ffcd13626f67fa2beff25cf337242d55857656292e326325490",
  "cid": "QmV191ca88761bbf3ffcd13626f67fa2beff25cf3372",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289659,
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
      "evaluated_at": 1760289659
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
  "sig": "af93f3a5be6d3724304c80bbce9438cc578fe9414e074e029cc1ec08154db646"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243232456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 43055556, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285765, 'matching_hash': '1b0a7dc1f650d378'}}}