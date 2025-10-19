```json
{
  "id": "04c8b7a8e37f74f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288664,
  "host_pid": "9e6742732c60:1",
  "hash": "88b3b948273218a5c745a7722fa503fdb433474cf1a761e31ec997b6ba10b89a",
  "cid": "QmV188b3b948273218a5c745a7722fa503fdb433474c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288664,
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
      "evaluated_at": 1760288664
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
  "sig": "2b2a6243ac8ee0b573a691134e4785c7967d576468470fd8d5e9ffdfc95e5d4f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153312612
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': 'b6b1aeb6185e45bf'}}}