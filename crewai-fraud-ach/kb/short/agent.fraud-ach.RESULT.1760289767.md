```json
{
  "id": "1b1549155b900135",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289767,
  "host_pid": "9e6742732c60:1",
  "hash": "f02eb8782f4dcb7be1ba86e157a397fd2d3376dd8948cc5c6cf2ea2cb10b9239",
  "cid": "QmV1f02eb8782f4dcb7be1ba86e157a397fd2d3376dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289767,
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
      "evaluated_at": 1760289767
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
  "sig": "3f9785feb4c4b1bf985f2cb8c781b5efb48b38309933e9e5193be47042259d1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022605707
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 36407448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285765, 'matching_hash': '50e001b692c48bf8'}}}