```json
{
  "id": "696d948abb21d8b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291491,
  "host_pid": "9e6742732c60:1",
  "hash": "8ce90692ad074f028cf95cf3bab28c72c8800befa46b35cc2725265f71f5cda9",
  "cid": "QmV18ce90692ad074f028cf95cf3bab28c72c8800bef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291491,
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
      "evaluated_at": 1760291492
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
  "sig": "636e3c03f99b5355aa83b0580f52b30b1b6c999cf51d9ebfd346ee2fd58668a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464887509
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 84813872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '8c09836a51c1ceac'}}}