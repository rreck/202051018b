```json
{
  "id": "25e1dafc0c039f12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293237,
  "host_pid": "9e6742732c60:1",
  "hash": "8e637ef36ef971fb1822145a05a4a87f86f3b65d4217c952c10104cc8ba7b4ec",
  "cid": "QmV18e637ef36ef971fb1822145a05a4a87f86f3b65d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293237,
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
      "evaluated_at": 1760293237
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
  "sig": "788b8098b03329a0cac31bf9ba347df78e599434ee6a6a076c8143b0b35b9ed4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469922578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 26261010, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '96901979868c282a'}}}