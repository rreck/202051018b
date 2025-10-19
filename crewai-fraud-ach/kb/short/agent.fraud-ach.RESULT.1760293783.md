```json
{
  "id": "c0f859252715b7c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293783,
  "host_pid": "9e6742732c60:1",
  "hash": "14a6908b09248b0a03909411dba90a9509aaf8d1f4ad7d076895732977476e8c",
  "cid": "QmV114a6908b09248b0a03909411dba90a9509aaf8d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293783,
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
      "evaluated_at": 1760293783
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
  "sig": "3adb11f6faf7355949061f3e671234c3ac04089d732016af03c0553c22da1260"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026908362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 11250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': '7a1f70b5e24e62dd'}}}