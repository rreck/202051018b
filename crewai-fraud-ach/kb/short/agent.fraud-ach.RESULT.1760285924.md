```json
{
  "id": "37949635bb94bfcf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285924,
  "host_pid": "9e6742732c60:1",
  "hash": "1c12ffddc2bb60a6d43c4b2ae4a35568b58a1db97088d661e74fbee849b12d58",
  "cid": "QmV11c12ffddc2bb60a6d43c4b2ae4a35568b58a1db9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285924,
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
      "evaluated_at": 1760285924
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
  "sig": "5ccdab2606d9c1dd14e2cdedffd5872ff270fbf3542166157999c92b7bd9c4b9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026725963
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285765, 'matching_hash': '729970816697b41b'}}}