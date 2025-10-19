```json
{
  "id": "d1d76da5b111d802",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289551,
  "host_pid": "9e6742732c60:1",
  "hash": "5b05c8bd1b7c7fc85714176d23d68c577b18592effdbdf923da657d37d3cb66e",
  "cid": "QmV15b05c8bd1b7c7fc85714176d23d68c577b18592e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289551,
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
      "evaluated_at": 1760289551
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
  "sig": "3ec44e2714fcf366c8fa4d6c03d9c6ca3ec285fff8cca3eb962d47a6a4c55a15"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155194168
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 46071270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285765, 'matching_hash': '7ab74b64ae25594e'}}}