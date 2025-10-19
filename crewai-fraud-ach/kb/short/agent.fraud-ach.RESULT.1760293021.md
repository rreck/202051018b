```json
{
  "id": "8954edfd010ef01a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293021,
  "host_pid": "9e6742732c60:1",
  "hash": "4d2bb454de62b55a5227406d04658d3d779b88b466cedf12fd9631fe4883c4da",
  "cid": "QmV14d2bb454de62b55a5227406d04658d3d779b88b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293021,
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
      "evaluated_at": 1760293021
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
  "sig": "855bc10925db1e1cb60f6d8408c4c0eb83fc0e2d17dad9aa25a14bd870108965"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 28040670, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}