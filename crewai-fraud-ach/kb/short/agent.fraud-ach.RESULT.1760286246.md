```json
{
  "id": "0264af4e3a559d02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286246,
  "host_pid": "9e6742732c60:1",
  "hash": "75300e78fcee1ab85fa1b01c057c455fe91e229e11f2fcc8762a5c24540ba252",
  "cid": "QmV175300e78fcee1ab85fa1b01c057c455fe91e229e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286246,
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
      "evaluated_at": 1760286246
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
  "sig": "249e77604b98b24e9bd16e3abb56cdaac671b74bde20680fb7a5b160dc4a6a4d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100271240415
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285765, 'matching_hash': '8c20097da64de4ba'}}}