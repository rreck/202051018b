```json
{
  "id": "fdca6c84454387f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293730,
  "host_pid": "9e6742732c60:1",
  "hash": "d903eb56274f6c50e70dd925213c9415333755de9f5f553bc7d12090ea2aee07",
  "cid": "QmV1d903eb56274f6c50e70dd925213c9415333755de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293730,
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
      "evaluated_at": 1760293730
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
  "sig": "af2f0c4520c12e0888dcfcc06cae4262a0d1fc3d3b473f75031f76c134a2e96f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029265266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 82228832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': 'a9619dd56a360910'}}}