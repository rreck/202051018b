```json
{
  "id": "a41485aa9ef3515f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287124,
  "host_pid": "9e6742732c60:1",
  "hash": "1ca9c78b4e1e80d551e1f5bbaa980e57385d8cca1324978d9377516e80990a8b",
  "cid": "QmV11ca9c78b4e1e80d551e1f5bbaa980e57385d8cca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287124,
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
      "evaluated_at": 1760287124
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
  "sig": "2176d3624ee89932d8d838b77ec0e6b411d811f823761432bbf82e39181fd8c3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591790243
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': '8c245acd6e70ddc0'}}}