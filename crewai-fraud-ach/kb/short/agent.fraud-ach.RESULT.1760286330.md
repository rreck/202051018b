```json
{
  "id": "d422cc583116cbc5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286330,
  "host_pid": "9e6742732c60:1",
  "hash": "51cc1559c5f5bbc2c175dec7e4d2c7fdd8fd4a366c5cbfce9948ff6dad0c4f87",
  "cid": "QmV151cc1559c5f5bbc2c175dec7e4d2c7fdd8fd4a36",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286330,
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
      "evaluated_at": 1760286330
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
  "sig": "ea161c2ebbd49addc7bd56e7fca07c832a6a695b8795f0b96339bbcafcef1cef"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469028209
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': 'a4269a968e85dafe'}}}