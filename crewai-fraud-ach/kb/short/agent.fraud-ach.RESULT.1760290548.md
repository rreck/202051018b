```json
{
  "id": "453727da068fc496",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290548,
  "host_pid": "9e6742732c60:1",
  "hash": "3985850a8015e096d67939c9fb0b9a05d30709c3a0e6764b3771a1a2fa75c635",
  "cid": "QmV13985850a8015e096d67939c9fb0b9a05d30709c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290548,
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
      "evaluated_at": 1760290548
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
  "sig": "4963a96e76fdc103cfce3a8f504dd071a6e0cb0a2d4396b6d6fd8534a09c0853"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028058978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285764, 'matching_hash': '1bb3ef3babc34591'}}}