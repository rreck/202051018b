```json
{
  "id": "536e54fee8ffcace",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293518,
  "host_pid": "9e6742732c60:1",
  "hash": "d1cbb6b174baadf8ac6440d5371c03698747476e36d44236abc6ea2d4faf4724",
  "cid": "QmV1d1cbb6b174baadf8ac6440d5371c03698747476e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293518,
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
      "evaluated_at": 1760293518
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
  "sig": "ad1809016734c33c1307c1041e0495b2e199fceb430a5ffae8646cbc620c705c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246221982
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 51196420, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '5c0c0fe7ab2d6845'}}}