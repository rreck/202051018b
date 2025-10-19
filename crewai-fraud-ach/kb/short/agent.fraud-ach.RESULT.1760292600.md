```json
{
  "id": "f6f9e28496bdf728",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292600,
  "host_pid": "9e6742732c60:1",
  "hash": "70df502cfd9c450cc2b7d9b7be0ba00838876553eeb866f36ca3e6c2702e1094",
  "cid": "QmV170df502cfd9c450cc2b7d9b7be0ba00838876553",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292600,
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
      "evaluated_at": 1760292600
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
  "sig": "8ffdfcbdb248065ca4c421897117111f54b5c1dc29daab8011cb3cd30c70e24c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273021249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 96931245, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285764, 'matching_hash': '8f9c0aaacb6951b9'}}}