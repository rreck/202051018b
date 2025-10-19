```json
{
  "id": "397ba5b87b4816db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287906,
  "host_pid": "9e6742732c60:1",
  "hash": "b9585054e36c2f426491babf8d4898ff1980be553e28cd18917002a028008351",
  "cid": "QmV1b9585054e36c2f426491babf8d4898ff1980be55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287906,
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
      "evaluated_at": 1760287906
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
  "sig": "5e7ed56fef37f54ca5baad5bc459cf715755c6da95303b726884d713866b51a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153312612
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': 'b6b1aeb6185e45bf'}}}