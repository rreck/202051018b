```json
{
  "id": "c97a88e8c7180962",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292087,
  "host_pid": "9e6742732c60:1",
  "hash": "65f9e975f041d666d423b63eeaecae9e88f4095e8593241f454e8d76199279f0",
  "cid": "QmV165f9e975f041d666d423b63eeaecae9e88f4095e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292087,
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
      "evaluated_at": 1760292087
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
  "sig": "f9078f5c163273a4a9166a40e44a3a341d854b796f0338e9de70db31277f9ac7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244516225
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 27858750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '305c81c4ba1c9c62'}}}