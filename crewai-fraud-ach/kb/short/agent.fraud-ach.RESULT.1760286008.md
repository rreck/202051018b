```json
{
  "id": "4df3a84c7c211821",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286008,
  "host_pid": "9e6742732c60:1",
  "hash": "ae5a75a4508b1a4142cbd91126fb39da034de70e40cc29213e87cc0c5e4a163d",
  "cid": "QmV1ae5a75a4508b1a4142cbd91126fb39da034de70e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286008,
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
      "evaluated_at": 1760286008
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
  "sig": "911af92978fcf6b032519bd733ca364a24b0b2ec7b91b67c7e2149a81abc6558"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000032270621
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285764, 'matching_hash': '380f2fccd8369f51'}}}