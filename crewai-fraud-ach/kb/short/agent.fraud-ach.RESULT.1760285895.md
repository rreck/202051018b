```json
{
  "id": "00044344e8064c7e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285895,
  "host_pid": "9e6742732c60:1",
  "hash": "2b399ea65939dfe18b14827afcb91318ce290406e8477defcf3031c4eb34e0e7",
  "cid": "QmV12b399ea65939dfe18b14827afcb91318ce290406",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285895,
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
      "evaluated_at": 1760285895
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
  "sig": "f1fc58cee72851bd8ea6bd743d23b79c788592576b4489801a3a89f3b4d56088"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241561723
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}