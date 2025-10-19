```json
{
  "id": "360757c4d14ebb9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294009,
  "host_pid": "9e6742732c60:1",
  "hash": "83b635762097559893dcc875242aaeb9816a4800bf6083e69096b4c45dc6d6d8",
  "cid": "QmV183b635762097559893dcc875242aaeb9816a4800",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294009,
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
      "evaluated_at": 1760294009
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
  "sig": "3c05f98e12472b8103514b7f76f36357f7054e74290a1f75ed7d7e109678c16f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272419137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 59450860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '38281b9a763b4bf2'}}}