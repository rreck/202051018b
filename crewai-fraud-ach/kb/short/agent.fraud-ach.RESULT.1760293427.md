```json
{
  "id": "0aad26bb54f99a16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293427,
  "host_pid": "9e6742732c60:1",
  "hash": "2539da637501c6360dafd70c1d98ca69050de2d143dbf24d9af242faac84cac0",
  "cid": "QmV12539da637501c6360dafd70c1d98ca69050de2d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293427,
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
      "evaluated_at": 1760293427
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
  "sig": "24decec383958566a79708b384f9ecff78978dfc31a1f65740aee22eeb610259"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467519914
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 26654860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': '8f358df1d478d699'}}}