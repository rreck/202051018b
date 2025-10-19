```json
{
  "id": "de0ca53e58e35a91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291890,
  "host_pid": "9e6742732c60:1",
  "hash": "64036521883c04705cd2766134b90644d913c436f0779d48b2984349c7561fcc",
  "cid": "QmV164036521883c04705cd2766134b90644d913c436",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291890,
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
      "evaluated_at": 1760291890
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "68a3aff416f0ec548a03740f932210b87ecc50106d2a773687b698040ffeaf16"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 1742172565, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.95, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9417149}}}