```json
{
  "id": "0cf25cc76860dc03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290318,
  "host_pid": "9e6742732c60:1",
  "hash": "4384d244b77a5c4a61ee98e125a3c480d8833907ec3e182208a87db0fee84ba9",
  "cid": "QmV14384d244b77a5c4a61ee98e125a3c480d8833907",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290318,
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
      "evaluated_at": 1760290319
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
  "sig": "cd667d3bb632a8fc92b1a692adbde4cb59ca8683279ce471f780f1216a75883f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279768309
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 18590395, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760284979, 'matching_hash': '8798983dc5a8227d'}}}