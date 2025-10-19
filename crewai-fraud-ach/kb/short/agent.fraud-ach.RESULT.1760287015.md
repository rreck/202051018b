```json
{
  "id": "fa7d79fad0c115dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287015,
  "host_pid": "9e6742732c60:1",
  "hash": "227a9a4286dc4d60e6f9dec09b9bcd7caae3e472b6825c35b1d180025475b60a",
  "cid": "QmV1227a9a4286dc4d60e6f9dec09b9bcd7caae3e472",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287015,
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
      "evaluated_at": 1760287015
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
  "sig": "df16109e87b3a007b1337603bf9effff40e2bb457b9c6e5ea3ed03310848223f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000039215537
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10871550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': '4decba5555bb1e33'}}}