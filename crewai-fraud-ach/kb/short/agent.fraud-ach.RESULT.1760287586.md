```json
{
  "id": "7f490364ffc41324",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287586,
  "host_pid": "9e6742732c60:1",
  "hash": "126f78324791023d861760464d5b9b00a921acd0800095cd15cb84c49c461194",
  "cid": "QmV1126f78324791023d861760464d5b9b00a921acd0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287586,
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
      "evaluated_at": 1760287586
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
  "sig": "ac47932875ec8f0dab46eba873e6ed0479234594030ee7fef4eeee7ff0cad7ef"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 021000027147487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 32487260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285765, 'matching_hash': 'f2056111b893f4fa'}}}