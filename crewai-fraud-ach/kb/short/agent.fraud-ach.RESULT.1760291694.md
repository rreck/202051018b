```json
{
  "id": "3726ccf839633c70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291694,
  "host_pid": "9e6742732c60:1",
  "hash": "4ee0066bca34b0a1d64827cb61f8cd5a23d2966b4150a38d4a8584836d02e243",
  "cid": "QmV14ee0066bca34b0a1d64827cb61f8cd5a23d2966b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291694,
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
      "evaluated_at": 1760291694
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
  "sig": "141fde73e64d3d4219f29e17738310627c42cd23e957910eb0c51ca14f22be09"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593787585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 78554905, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '27c7bfe810f6d733'}}}