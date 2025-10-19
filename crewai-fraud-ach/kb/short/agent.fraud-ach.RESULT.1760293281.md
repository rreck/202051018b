```json
{
  "id": "a8e699b22963e344",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293281,
  "host_pid": "9e6742732c60:1",
  "hash": "3f1093bd853be77f89a2ba024dced01f0d92037411cc07d42d2fcf966e3bda10",
  "cid": "QmV13f1093bd853be77f89a2ba024dced01f0d920374",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293281,
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
      "evaluated_at": 1760293281
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
  "sig": "9a33e824be9a4ee69d8a3a5442e81a534b8974289c5a032407ef41cd7c0098bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030146217
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 291, 'threshold': 50, 'total_amount': 140372871, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 290, 'first_seen': 1760284979, 'matching_hash': '16ae1b567cc6df9d'}}}