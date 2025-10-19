```json
{
  "id": "c53ddd90de4fa3f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289708,
  "host_pid": "9e6742732c60:1",
  "hash": "11b17bbca0ae9e0e605f5691baf4f4ecdab96fb538e29119e98db01097831bca",
  "cid": "QmV111b17bbca0ae9e0e605f5691baf4f4ecdab96fb5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289708,
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
      "evaluated_at": 1760289708
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
  "sig": "97a1d94708cf77cff054f725b6ed850b728a68ac1528ace4f21baab1f8745cbd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596228343
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 13100000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '964edcfaddb10414'}}}