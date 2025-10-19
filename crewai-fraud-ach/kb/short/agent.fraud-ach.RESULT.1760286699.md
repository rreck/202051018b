```json
{
  "id": "9bb9ebd361f8d233",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286699,
  "host_pid": "9e6742732c60:1",
  "hash": "31eb2a35af934f2b73e40a636773a37d050f1cc319c2721bdc4d687416bc53db",
  "cid": "QmV131eb2a35af934f2b73e40a636773a37d050f1cc3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286699,
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
      "evaluated_at": 1760286699
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "5be11aa6463598da5372665f7fe5d2523fc08b07d675efdbe9d0435dd850c6a7"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000241821144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16677544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '9191e5c904ced497'}}}760284979, 'matching_hash': 'ed66d17e763eb837'}}}