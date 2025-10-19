```json
{
  "id": "d4e770faf01414ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286281,
  "host_pid": "9e6742732c60:1",
  "hash": "89c86defb8430f5831ecf6ae362ffb2fd1e17f93b240cb0afd2842f3aca274a3",
  "cid": "QmV189c86defb8430f5831ecf6ae362ffb2fd1e17f93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286281,
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
      "evaluated_at": 1760286281
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
  "sig": "4d123ee2ac3fe0fbee8c523446815fc7882344c5b46243ba6a1b54116a172dfe"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000036177444
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285764, 'matching_hash': '11850a408d1201a4'}}}