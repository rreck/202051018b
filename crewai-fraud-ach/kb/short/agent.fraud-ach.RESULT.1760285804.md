```json
{
  "id": "a3fb26d6877778ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285804,
  "host_pid": "9e6742732c60:1",
  "hash": "6fb847cc77bbfd89c04271f08cc49d0b855c7645617afeeace1ccc34ffe10c35",
  "cid": "QmV16fb847cc77bbfd89c04271f08cc49d0b855c7645",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285804,
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
      "evaluated_at": 1760285804
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
  "sig": "46292a037723de4799d801df66f372c34f9abcf0aa41a6980337cda72ecc15a9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245693870
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285763, 'matching_hash': '3f6bcdf181d34e46'}}}k_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760284979, 'matching_hash': 'b9497544c8340a37'}}}