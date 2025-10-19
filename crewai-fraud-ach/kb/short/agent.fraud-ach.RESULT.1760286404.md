```json
{
  "id": "2d48c7857772ba0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286404,
  "host_pid": "9e6742732c60:1",
  "hash": "c887c5a79519a12f9cf87e484faa1952136e9a3ccf9918a0fbfcfb2b5097b719",
  "cid": "QmV1c887c5a79519a12f9cf87e484faa1952136e9a3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286404,
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
      "evaluated_at": 1760286404
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
  "sig": "2eaefb2c2a7bdd2d8971d9f665d9005026a50d1f290fdbdc08ed8a87d421a7e5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242987850
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285764, 'matching_hash': 'ac2312cc15fe4af9'}}}