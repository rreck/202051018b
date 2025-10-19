```json
{
  "id": "910bf26650e6225a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290590,
  "host_pid": "9e6742732c60:1",
  "hash": "756745ca713e4daa9a3045034b468a18233bff94aa590f9d09b14ea2e8c7f010",
  "cid": "QmV1756745ca713e4daa9a3045034b468a18233bff94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290590,
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
      "evaluated_at": 1760290590
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
  "sig": "f1790b0fc75d3e9c40a7611bc9b78f843a047550de12a38a62526bd267ffd446"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157447901
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 20823726, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}