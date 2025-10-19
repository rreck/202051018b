```json
{
  "id": "9cca42a2aae48a86",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286310,
  "host_pid": "9e6742732c60:1",
  "hash": "bae8f929e395582ec44082b80d8dc8c3ec1283655b82b9eafe7203038089d685",
  "cid": "QmV1bae8f929e395582ec44082b80d8dc8c3ec128365",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286310,
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
      "evaluated_at": 1760286310
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
  "sig": "0a62e82d2cd8353b5d0300d30d3cf714c9a63cf0f059f63206d8527c8380e885"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000038607326
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285763, 'matching_hash': '23e85c6499cf881c'}}}