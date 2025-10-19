```json
{
  "id": "268c2fc57bc415ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290302,
  "host_pid": "9e6742732c60:1",
  "hash": "6779a6e194e93519c43a645879ba8d609669632cce9ec88a55ebf2d113de85ad",
  "cid": "QmV16779a6e194e93519c43a645879ba8d609669632c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290302,
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
      "evaluated_at": 1760290302
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
  "sig": "a565064f4e6dd3fd5514a95693f39fdfe8675faccc01d79ffea28da011e4ae13"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591034480
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 59810331, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '8ba7f443842400ac'}}}