```json
{
  "id": "13e5e0abafab5110",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285942,
  "host_pid": "9e6742732c60:1",
  "hash": "f76c67929a7e4da73c73786f26421addd7e0b4395caa642f3e0c4bf33ec5a42d",
  "cid": "QmV1f76c67929a7e4da73c73786f26421addd7e0b439",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285942,
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
      "evaluated_at": 1760285942
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
  "sig": "f95943ef537c57ac1190a3d2b823057c25d079683ecc53a5e70cae612d828b5e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245084656
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285763, 'matching_hash': '11924a0da29b01ce'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}