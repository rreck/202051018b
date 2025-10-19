```json
{
  "id": "11e0ea3446a4c2c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293928,
  "host_pid": "9e6742732c60:1",
  "hash": "b13ea7b17c2fa67eee0b15694d0b3ace14029db3f1d492caeee7fc76cec598de",
  "cid": "QmV1b13ea7b17c2fa67eee0b15694d0b3ace14029db3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293928,
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
      "evaluated_at": 1760293928
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
  "sig": "079c4883ce00082f9c81cc1400aa15133df896baddddad97e365d524b6568e33"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024587821
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 98408448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': 'e3fd1743fc412dec'}}}}