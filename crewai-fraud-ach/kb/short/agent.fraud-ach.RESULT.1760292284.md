```json
{
  "id": "a5ee7dc30db47aa2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292284,
  "host_pid": "9e6742732c60:1",
  "hash": "7e3270e2318b0139846e5bc6f7850ebf5d153b48391b68afffacb21df1637b04",
  "cid": "QmV17e3270e2318b0139846e5bc6f7850ebf5d153b48",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292284,
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
      "evaluated_at": 1760292284
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
  "sig": "9563fd193a184906b56fc00dd1c2bbd75cd4fca4626c076db7dfaa67e3ef8aa5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597950940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 51684898, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'cd3d42208c2780a3'}}}