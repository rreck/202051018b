```json
{
  "id": "8b0a38b0ab906840",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291409,
  "host_pid": "9e6742732c60:1",
  "hash": "c5b9664f0c3831be481fe68704f84d231db7381332123fe56b91c357d63c73fa",
  "cid": "QmV1c5b9664f0c3831be481fe68704f84d231db73813",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291409,
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
      "evaluated_at": 1760291409
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
  "sig": "ff5c2fe076d19959e0ea81313248b4241c0ee1e5357e5777cfdf70fef5f97196"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 45482382, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}