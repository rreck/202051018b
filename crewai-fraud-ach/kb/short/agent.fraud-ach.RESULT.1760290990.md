```json
{
  "id": "be3fae2d32a767aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290990,
  "host_pid": "9e6742732c60:1",
  "hash": "256e85efc2bf1c95927bfe01a090ffa915a5be24085b6407f47798ef50eb5dca",
  "cid": "QmV1256e85efc2bf1c95927bfe01a090ffa915a5be24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290990,
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
      "evaluated_at": 1760290990
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
  "sig": "1b7192199b4c9016e995cb13dcf7fff4d9cae238f9424375b1baf6274379f7cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598500621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 58485024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '36e427bddf577026'}}}