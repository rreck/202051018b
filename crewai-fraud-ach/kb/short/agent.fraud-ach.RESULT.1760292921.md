```json
{
  "id": "c979f12f89db1e29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292921,
  "host_pid": "9e6742732c60:1",
  "hash": "0481604d9b5098024eb09656197c333f8e002b30149f5bc9d38db0f61ef4ef03",
  "cid": "QmV10481604d9b5098024eb09656197c333f8e002b30",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292921,
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
      "evaluated_at": 1760292921
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
  "sig": "fd0642ad7bcd87b2bcc6d36dc6f95555406541abd029f1a30858133b0118580e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598639172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 10400000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': '9f277109cf79f7ea'}}}