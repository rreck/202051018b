```json
{
  "id": "d0b870fe8b28dd91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293294,
  "host_pid": "9e6742732c60:1",
  "hash": "2991a6c4a641c85b8a16a89d9422a11a5320f92af6bdecdf9d6a642a1462dcf0",
  "cid": "QmV12991a6c4a641c85b8a16a89d9422a11a5320f92a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293294,
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
      "evaluated_at": 1760293294
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
  "sig": "f046f770c3253052437c54989dd6e59ecd3e16736961a4c6af19e3496816b5d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025375881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 14195805, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': '7f563b0766db4821'}}}