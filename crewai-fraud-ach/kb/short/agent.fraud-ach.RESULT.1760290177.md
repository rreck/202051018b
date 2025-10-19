```json
{
  "id": "083a21998e37b894",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290177,
  "host_pid": "9e6742732c60:1",
  "hash": "17f63ee503ae806a60c004a41107cd24323793bea8ee3a1ac9e0ad20a285c272",
  "cid": "QmV117f63ee503ae806a60c004a41107cd24323793be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290177,
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
      "evaluated_at": 1760290177
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
  "sig": "5757d5516b43abc7a271f9237cce62b0f9c2f5cb53630927901a6e65ddcf094b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029386599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 12022868, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}